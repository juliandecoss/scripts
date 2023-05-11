
resource "aws_security_group" "sg_back_server" {

  name        = "back server sg"
  description = "Allow http and https inbound traffic"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description     = "allow SSH"
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "allow HTTP"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description      = "allow HTTP from ipv6"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    ipv6_cidr_blocks = ["::/0"]
  }
}

# wordpress ec2 instance
resource "aws_instance" "back_server" {
  ami                    = "ami-00f7e5c52c0f43726"
  instance_type          = "t2.micro"
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.sg_back_server.id]
  subnet_id              = module.vpc.public_subnets[0]
  # user_data              = <<EOF
  # #! /bin/bash
  # sudo apt update
  # sudo snap install core; sudo snap refresh core
  # sudo snap install --classic certbot
  # sudo ln -s /snap/bin/certbot /usr/bin/certbot
  # EOF

  tags = {
    Name = "Back Server"
  }
}

output "back_server_ip" {
  value = aws_instance.back_server.private_ip
}
