
CREATE TABLE guilds (
    guild_id BIGINT NOT NULL
    
)

CREATE TABLE guild_settings (
    muted_role INT(20) DEFAULT 'Muted',
    guild_prefix VARCHAR(15) DEFAULT 'u!',
    log_channel INT(20) DEFAULT NULL,
    join_channel INT(20) DEFAULT NULL,
    leave_channel INT(20) DEFAULT NULL,
    PRIMARY KEY (log_channel, join_channel, leave_channel)

)