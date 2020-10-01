FROM python:3.6-onbuild

ADD utilitybot.py /

ADD /utils /

ADD /cogs /

ADD /events /


ENTRYPOINT [ "python" ]

CMD ["./utilitybot.py" ]