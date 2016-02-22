import placebo
from awslogs.core import AWSLogs


def test_get_groups():
    alogs = AWSLogs()
    session = alogs.session
    data_path = "tests/recorded/abcdefg"
    pill = placebo.attach(session, data_path=data_path)
    pill.playback()
    groups = list(alogs.get_groups())
    pill.stop()
    assert groups == ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def test_describe_log_groups():
    import boto3
    session = boto3.Session()
    data_path = "tests/recorded/abcdefg"
    pill = placebo.attach(session, data_path=data_path)
    client = session.client("logs")
    pill.playback()
    resp = client.describe_log_groups()
    pill.stop()
    assert resp["logGroups"][0]["logGroupName"] == "A"
