FROM python

WORKDIR /app

# Don't "ADD ." because that will cause pip install to rerun if anything in
# directory changes.
ADD requirements.txt /app
RUN pip install -r requirements.txt

ADD indexer.py /app
CMD ["python", "indexer.py"]
