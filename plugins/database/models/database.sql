CREATE TABLE guilds (
    
    guild_id BIGINT NOT NULL DEFAULT 0
)

CREATE TABLE guild_settings (
    guild_prefix VARCHAR(15) DEFAULT 'u!',
    log_channel VARCHAR(20),
    join_channel VARCHAR(20),
    leave_channel VARCHAR(20),
    PRIMARY KEY (guild_prefix, log_channel, join_channel, leave_channel)

)