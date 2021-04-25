FROM ubuntu:latest

RUN apt-get update && apt-get -y install cron

# Copy hello-cron file to the cron.d directory
COPY rec-cron /etc/cron.d/rec-cron
 
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/rec-cron

# Apply cron job
RUN crontab /etc/cron.d/rec-cron
 
# Create the log file to be able to run tail
RUN touch /var/log/cron.log
 
# Run the command on container startup
CMD cron && tail -f /var/log/cron.log