python tfgen.py
terraform init
terraform apply -auto-approve
terraform output -json > output.json
chmod +x update-dns.py
python update-dns.py
