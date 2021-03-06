#!/usr/bin/env cwl-runner
class: CommandLineTool
cwlVersion: v1.1.0-dev1
doc: "Test of capturing stderr output in a docker container."
hints:
  DockerRequirement:
    dockerPull: debian:wheezy

inputs: []

outputs:
  output_file:
    type: stderr

baseCommand: egrep
successCodes: [2]

stderr: std.err
