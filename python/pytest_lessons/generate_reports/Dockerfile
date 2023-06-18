# Используем базовый образ с установленной Java
FROM openjdk:8-jre

# Устанавливаем необходимые зависимости
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean

# Устанавливаем Allure
RUN curl -o allure-2.15.0.tgz -Ls https://github.com/allure-framework/allure2/releases/download/2.15.0/allure-2.15.0.tgz && \
    tar -zxvf allure-2.15.0.tgz -C /opt/ && \
    rm allure-2.15.0.tgz && \
    ln -s /opt/allure-2.15.0/bin/allure /usr/bin/allure

# Указываем порт, который будет использоваться Allure
ENV ALLURE_PORT 8080
EXPOSE $ALLURE_PORT

# Запускаем Allure-сервер
CMD ["sh", "-c", "allure serve --port 8080"]