CREATE TABLE guilds (
    
    guild_id BIGINT NOT NULL DEFAULT 0
)

CREATE TABLE guild_settings (
    guild_prefix VARCHAR(15) DEFAULT 'u!',
    log_channel INT(20) DEFAULT NULL,
    join_channel INT(20) DEFAULT NULL,
    leave_channel INT(20) DEFAULT NULL,
    PRIMARY KEY (guild_prefix, log_channel, join_channel, leave_channel)

)