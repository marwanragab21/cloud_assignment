#base image
FROM python
ENV DIR=/hamo
COPY . $hamo
WORKDIR $hamo
CMD python pyfile.py 
