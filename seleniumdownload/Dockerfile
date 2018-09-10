FROM python:3-slim

# firefox dependencies
RUN apt-get update && \
    apt-get install -y `apt-cache depends firefox-esr | awk '/Depends:/{print$2}'` curl bzip2 &&\
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# set firefox and geckodriver versions
ENV FIREFOX_VERSION 62.0
ENV GECKODRIVER_VERSION v0.21.0

# install firefox binary
RUN curl -L https://download-installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/pt-BR/firefox-$FIREFOX_VERSION.tar.bz2 | tar xj &&\
    mv firefox /opt/firefox/ && ln -s /opt/firefox/firefox /usr/bin/firefox

# install geckodriver binary
RUN curl -L https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz | tar xz &&\
    mv geckodriver /usr/bin/geckodriver

# set firefox headless
ENV MOZ_HEADLESS 1

# install pipenv
RUN pip install pipenv --upgrade

# copy and install app
WORKDIR /app
COPY . /app
RUN pipenv install --deploy --system

# execute main
CMD ["python", "main.py"]
