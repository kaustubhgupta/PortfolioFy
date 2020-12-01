FROM python:3

RUN pip install -Iv PyGithub==1.53
COPY ./ /PortfolioFy

ENTRYPOINT ["python", "/gen_index/generate_index.py"]