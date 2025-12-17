from typing import Any, Dict, Optional
from threading import Lock
import time

_lock = Lock()

# job_id -> status info
_JOBS: Dict[str, Dict[str, Any]] = {}

# job_id -> result
_RESULTS: Dict[str, Dict[str, Any]] = {}

def create_job(job_id: str, config: Dict[str, Any]) -> None:
    with _lock:
        _JOBS[job_id] = {
            "job_id": job_id,
            "status": "PENDING",
            "progress": 0.0,
            "created_at": time.time(),
            "config": config,
            "error": None,
        }

def update_job(job_id: str, status: str, progress: Optional[float] = None, error: Optional[str] = None) -> None:
    with _lock:
        job = _JOBS.get(job_id)
        if not job:
            return
        job["status"] = status
        if progress is not None:
            job["progress"] = progress
        if error is not None:
            job["error"] = error

def get_job(job_id: str) -> Optional[Dict[str, Any]]:
    with _lock:
        return _JOBS.get(job_id)

def save_result(job_id: str, result: Dict[str, Any]) -> None:
    with _lock:
        _RESULTS[job_id] = result

def get_result(job_id: str) -> Optional[Dict[str, Any]]:
    with _lock:
        return _RESULTS.get(job_id)
