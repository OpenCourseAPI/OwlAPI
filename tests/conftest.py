import pytest


@pytest.fixture(scope="class")
def fix_snapshots(request):
    """
    Hotpatch to fix a bug in snapshottest where the should_update flag is hardcoded

    Use on snapshottest.UnitTest subclasses as
    `@pytest.mark.usefixtures('fix_snapshots')`
    """
    request.cls.snapshot_should_update = request.config.option.snapshot_update
