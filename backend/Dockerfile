# Usamos la imagen oficial de Alpine como base
FROM alpine-gns3:latest

# Establecer el directorio de trabajo
WORKDIR /app

# Copy src code
COPY . /app/

# Port config
EXPOSE 5000

CMD ["python3", "app.py"]
