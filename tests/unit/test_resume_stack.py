import json
import pytest

from aws_cdk import core
from resume.resume_stack import ResumeStack


def get_template():
    app = core.App()
    ResumeStack(app, "resume")
    return json.dumps(app.synth().get_stack("resume").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
