from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

def child_exit(server, worker):
    """
    function for gunicorn
    """
    GunicornInternalPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)
