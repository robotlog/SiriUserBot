# Faster & Secure & Special Container #
# Thanks to mkaraniya & zakaryan2004
# Ve yusufusta'ya teşekkürler

FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/robotlog/Siriuserbot /root/siriuserbot 
WORKDIR /root/siriuserbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
