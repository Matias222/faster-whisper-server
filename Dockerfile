FROM debian:11.6

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /code

RUN apt-get update && \
    apt-get install -y libglib2.0 &&\
    apt-get install -y libglib2.0-cil &&\
    apt-get install -y libglib2.0-cil-dev &&\
    apt-get install -y --no-install-recommends \
        python3 python3-pip python3-dev \
        libgirepository1.0 libasound2 \
        libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly python3-gst-1.0 \
        apt-transport-https curl

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apt-get install -y ffmpeg

COPY ./app /code/app

#RUN python3 -c "from faster_whisper import WhisperModel; WhisperModel('small', device='cpu', compute_type='int8')"

RUN python3 -c "from faster_whisper import WhisperModel; WhisperModel('small', device='cuda', compute_type='float16')"

EXPOSE 80

CMD ["fastapi", "run", "app/main.py", "--port", "80"]