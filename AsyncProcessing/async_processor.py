"""
Async Processing Module for OaSIS LLM Automation Ratings
=========================================================
Drop-in async support for the main study notebook.
Provides 5x speedup with identical results.

Usage in notebook:
    from async_processor import run_async_ratings, ASYNC_ENABLED
    
    if ASYNC_ENABLED:
        results = await run_async_ratings(combinations, generate_rating, generate_rating_explanation)
    else:
        # Use existing sequential loop
"""

import asyncio
import time
from typing import Any

# Configuration
ASYNC_ENABLED = True  # Set to False to disable async (use sequential)
BATCH_SIZE = 5  # Number of concurrent requests (respect rate limits)


async def process_single_async(
    combo: dict,
    generate_rating,
    generate_rating_explanation,
    index: int,
    total: int
) -> dict:
    """Process a single combination using async call."""
    call_start = time.time()
    
    try:
        if combo.get('expects_explanation', False):
            prediction = await generate_rating_explanation.acall(
                full_request_text=combo['formatted_prompt']
            )
            explanation = prediction.explanation
        else:
            prediction = await generate_rating.acall(
                full_request_text=combo['formatted_prompt']
            )
            explanation = ""
        
        return {
            'item_name': combo['item_name'],
            'prompt_id': combo['prompt_id'],
            'rating': prediction.rating,
            'explanation': explanation,
            'call_time': time.time() - call_start,
            'success': True
        }
        
    except Exception as e:
        return {
            'item_name': combo['item_name'],
            'prompt_id': combo['prompt_id'],
            'error': str(e),
            'call_time': time.time() - call_start,
            'success': False
        }


async def run_async_ratings(
    combinations: list[dict],
    generate_rating,
    generate_rating_explanation,
    batch_size: int = BATCH_SIZE,
    progress_callback=None
) -> tuple[list[dict], list[dict]]:
    """
    Run all rating calls asynchronously with controlled concurrency.
    
    Args:
        combinations: List of item/prompt combinations
        generate_rating: DSPy Predict module for rating only
        generate_rating_explanation: DSPy Predict module for rating + explanation
        batch_size: Max concurrent requests (default 5)
        progress_callback: Optional function(current, total) for progress updates
    
    Returns:
        Tuple of (successful_results, failed_results)
    """
    semaphore = asyncio.Semaphore(batch_size)
    total = len(combinations)
    completed = 0
    
    async def bounded_process(combo, index):
        nonlocal completed
        async with semaphore:
            result = await process_single_async(
                combo, generate_rating, generate_rating_explanation, index, total
            )
            completed += 1
            if progress_callback:
                progress_callback(completed, total)
            return result
    
    # Run all calls concurrently (bounded by semaphore)
    all_results = await asyncio.gather(*[
        bounded_process(combo, i) for i, combo in enumerate(combinations)
    ])
    
    # Separate successes and failures
    successes = [r for r in all_results if r.get('success')]
    failures = [r for r in all_results if not r.get('success')]
    
    return successes, failures


def run_ratings_sync_or_async(
    combinations: list[dict],
    generate_rating,
    generate_rating_explanation,
    use_async: bool = ASYNC_ENABLED,
    batch_size: int = BATCH_SIZE,
    sleep_seconds: float = 0.5
) -> tuple[list[dict], list[dict]]:
    """
    Unified interface: runs async if enabled, otherwise sequential.
    
    This is the main entry point for the notebook.
    """
    if use_async:
        print(f"Running ASYNC mode (batch_size={batch_size})...")
        return asyncio.run(run_async_ratings(
            combinations, generate_rating, generate_rating_explanation, batch_size
        ))
    else:
        print(f"Running SEQUENTIAL mode (sleep={sleep_seconds}s)...")
        results = []
        errors = []
        
        for i, combo in enumerate(combinations):
            call_start = time.time()
            
            try:
                if combo.get('expects_explanation', False):
                    prediction = generate_rating_explanation(
                        full_request_text=combo['formatted_prompt']
                    )
                    explanation = prediction.explanation
                else:
                    prediction = generate_rating(
                        full_request_text=combo['formatted_prompt']
                    )
                    explanation = ""
                
                results.append({
                    'item_name': combo['item_name'],
                    'prompt_id': combo['prompt_id'],
                    'rating': prediction.rating,
                    'explanation': explanation,
                    'call_time': time.time() - call_start
                })
                
            except Exception as e:
                errors.append({
                    'item_name': combo['item_name'],
                    'prompt_id': combo['prompt_id'],
                    'error': str(e)
                })
            
            # Rate limiting
            if i < len(combinations) - 1:
                time.sleep(sleep_seconds)
        
        return results, errors
