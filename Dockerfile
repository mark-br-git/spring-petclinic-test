# Use the official OpenJDK 11 image as the base image
FROM openjdk:17

# Set the working directory inside the container
WORKDIR /app

# Copy the Spring Boot application jar file to the container
COPY target/spring-petclinic-3.1.0-SNAPSHOT.jar /app/spring-petclinic.jar

# Expose the port on which the application will listen
EXPOSE 8080

# Define the command to run the Spring Boot application
CMD ["java", "-jar", "spring-petclinic.jar"]
