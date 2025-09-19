FROM python:3.12-slim

# Sistem bağımlılıkları
RUN apt-get update && apt-get install -y git curl dos2unix && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Proje bağımlılıkları
COPY requirements.txt ./

# OVOS Core kurulumu
RUN git clone https://github.com/OpenVoiceOS/ovos-core.git
WORKDIR /app/ovos-core
RUN python3 -m venv .venv

RUN /app/ovos-core/.venv/bin/pip install --no-cache-dir -r requirements/requirements.txt && /app/ovos-core/.venv/bin/python setup.py install


# Proje bağımlılıklarını kur
WORKDIR /app
RUN /app/ovos-core/.venv/bin/pip install --no-cache-dir -r /app/requirements.txt
RUN mkdir -p /root/.local/share/mycroft/skills/my_weather_skill.skill
RUN chown -R root:root /root/.local/share/mycroft/skills
RUN chmod -R 755 /root/.local/share/mycroft/skills

# Skill'leri kopyala

RUN mkdir -p /root/.local/share/mycroft/skills
COPY skills/my_weather_skill /app/skills/my_weather_skill
COPY skills/my_weather_skill /root/.local/share/mycroft/skills/my_weather_skill.skill/
RUN dos2unix -r /app/skills/my_weather_skill || true 
RUN dos2unix -r /root/.local/share/mycroft/skills/my_weather_skill.skill || true


RUN /app/ovos-core/.venv/bin/pip install --no-cache-dir /app/skills/my_weather_skill 
 
RUN chown -R root:root /root/.local/share/mycroft/skills/my_weather_skill.skill
RUN chmod -R 755 /root/.local/share/mycroft/skills/my_weather_skill.skill

# Başlatma scriptini kopyala
COPY start.sh .
RUN chmod +x start.sh

COPY mycroft.conf /root/.config/mycroft/mycroft.conf 
ENV XDG_CONFIG_HOME=/root/.config \
    XDG_DATA_HOME=/root/.local/share \
    MYCROFT_SKILLS_DIR=/root/.local/share/mycroft/skills \
    OVOS_SKILLS_DIR=/root/.local/share/mycroft/skills
EXPOSE 8181

CMD ["bash", "start.sh"]


