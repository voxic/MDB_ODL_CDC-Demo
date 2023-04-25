provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "ec2" {
  ami = "ami-07bdb714a483cb3bc"
  instance_type = "t3.medium"
  key_name = "<your private key>"
  vpc_security_group_ids = ["<your security group>"]
  tags = {
    Name = "<instance name>",
    owner = "<your name>",
    expires-on = "<expires-on>",
    purpose = "<your purpose>"
  }

  user_data = <<EOF
    #!/bin/bash
    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo service docker start
    sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo usermod -a -G docker ec2-user
    sudo curl -L https://raw.githubusercontent.com/voxic/cdc_public/main/docker-compose.yaml -o /home/ec2-user/docker-compose.yaml
    sudo mkdir /root/connectors
    sudo curl -L https://github.com/mongodb/mongo-kafka/releases/download/r1.9.0/mongodb-kafka-connect-mongodb-1.9.0.zip -o /root/connectors/mongodb-kafka-connect-mongodb-1.9.0.zip
    sudo unzip /root/connectors/mongodb-kafka-connect-mongodb-1.9.0.zip -d /root/connectors/
    sudo /usr/local/bin/docker-compose -f /home/ec2-user/docker-compose.yaml up -d
    EOF
}
