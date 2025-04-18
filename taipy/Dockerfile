# Your Python version
FROM python:3.9 as taipy

# Web port of the application
EXPOSE 5000

# Create taipy user for security
RUN groupadd -r taipy && useradd -r -m -g taipy taipy


# Go to the dedicated folder and add the python corresponding folder in PATH
WORKDIR /workspaces
ENV PATH="${PATH}:/workspaces/.local/bin"

# Update pip
RUN python -m pip install --upgrade pip

# Install application's dependencies
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Install your application
COPY . .

COPY --chown=taipy:taipy entrypoint.sh workspaces

RUN chmod +x /workspaces/entrypoint.sh
USER taipy

ENTRYPOINT ["/workspaces/entrypoint.sh"]