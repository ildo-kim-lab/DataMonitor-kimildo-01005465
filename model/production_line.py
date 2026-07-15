import math
import time
from collections import deque


class ProductionJob:
    def __init__(self, order, sample, shortage_quantity):
        self.order = order
        self.sample = sample
        self.shortage_quantity = shortage_quantity
        self.actual_quantity = math.ceil(shortage_quantity / sample.yield_rate)
        self.total_time = sample.avg_production_time * self.actual_quantity
        self.start_time = None

    @property
    def produced_quantity(self):
        """생산 시작 시각부터의 경과 시간을 총 생산 시간과 비교해 실시간으로 계산한다."""
        if self.start_time is None or self.total_time <= 0:
            return 0
        elapsed = time.time() - self.start_time
        ratio = min(elapsed / self.total_time, 1.0)
        return math.floor(self.actual_quantity * ratio)

    def is_finished(self):
        return self.produced_quantity >= self.actual_quantity


class ProductionLine:
    """하나의 생산 라인은 시료를 하나씩(FIFO) 생산한다."""

    def __init__(self):
        self._queue = deque()
        self._current_job = None

    def enqueue(self, job: ProductionJob):
        self._queue.append(job)
        if self._current_job is None:
            self._start_next()

    def _start_next(self):
        self._current_job = self._queue.popleft() if self._queue else None
        if self._current_job is not None:
            self._current_job.start_time = time.time()

    def current_job(self):
        return self._current_job

    def queued_jobs(self):
        return list(self._queue)

    def complete_current_job(self):
        job = self._current_job
        if job is None:
            return None
        self._start_next()
        return job
