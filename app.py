#!/usr/bin/env python3

from aws_cdk import core

from resume.resume_stack import ResumeStack


app = core.App()
ResumeStack(app, "resume", env={'region': 'us-west-2'})

app.synth()
