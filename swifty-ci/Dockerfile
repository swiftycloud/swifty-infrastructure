FROM fedora:27

LABEL maintainer="Vladimir Grevtsev vlgrevtsev@gmail.com"

WORKDIR /home

RUN mkdir ~/.ssh && echo -e "Host *  \n StrictHostKeyChecking no" > ~/.ssh/config
RUN dnf install -y ansible wget unzip python-virtualenv git
RUN pip install awscli
RUN wget https://releases.hashicorp.com/terraform/0.11.10/terraform_0.11.10_linux_amd64.zip -O terraform.zip && \
    unzip terraform.zip && mv terraform /usr/local/bin
RUN virtualenv .env

CMD ["bash"]