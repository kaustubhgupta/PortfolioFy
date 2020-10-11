FROM python:3

RUN pip install -Iv PyGithub==1.53
COPY ./ /gen_index

ENTRYPOINT ["python", "/gen_index/generate_index.py"]