FROM odoo:18.0

USER root

WORKDIR /opt/odoo
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt  --break-system-packages

USER odoo

CMD ["odoo"]