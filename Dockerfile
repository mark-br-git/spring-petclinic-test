## Build Stage ###
FROM maven:3.8.3-openjdk-17 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy the whole project to the container
COPY . .

# Build the Spring Petclinic application using Maven
RUN mvn clean package -DskipTests

### Runtime Stage ###
FROM eclipse-temurin:17-jre-jammy

# Set the working directory inside the container
WORKDIR /app

# Copy the Spring Petclinic JAR file from the build stage to the runtime stage
COPY --from=build /app/target/spring-petclinic-3.1.0-SNAPSHOT.jar /app/spring-petclinic.jar

# Expose the port that your application listens on (if applicable)
EXPOSE 8080

# Define the command to run your application
CMD ["java", "-jar", "spring-petclinic.jar"]
