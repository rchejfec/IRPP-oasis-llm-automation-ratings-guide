# Async Processing Integration Guide

## Quick Start

Add these cells to your notebook to enable 5x faster processing:

### Cell 1: Import async module (after DSPy setup)

```python
# Async processing support (5x speedup)
from async_processor import run_ratings_sync_or_async, ASYNC_ENABLED, BATCH_SIZE

print(f"Async mode: {'ENABLED' if ASYNC_ENABLED else 'DISABLED'}")
print(f"Batch size: {BATCH_SIZE}")
```

### Cell 2: Replace the processing loop

```python
# Replace the existing sequential loop with:
import time

start_time = time.time()
results, errors = run_ratings_sync_or_async(
    combinations,
    generate_rating,
    generate_rating_explanation,
    use_async=True,  # Set to False for sequential
    batch_size=5
)
elapsed = time.time() - start_time

print(f"Completed {len(results)} calls in {elapsed:.1f}s")
print(f"Errors: {len(errors)}")
```

## Configuration

Edit `async_processor.py` to change defaults:

```python
ASYNC_ENABLED = True   # Toggle async on/off
BATCH_SIZE = 5         # Concurrent requests (respect rate limits)
```

## Requirements

- Paid API tier (higher rate limits)
- DSPy with async support
