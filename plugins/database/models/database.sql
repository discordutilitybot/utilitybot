
CREATE TABLE guilds (
    guild_id INT(20) NOT NULL DEFAULT 0,
    guild_roles BIGINT NOT NULL DEFAULT 0,
    guild_channels BIGINT NOT NULL DEFAULT 0
    guild_messages BIGINT NOT NULL DEFAULT 0

)

CREATE TABLE guild_settings (
    muted_role INT(20) DEFAULT 'Muted',
    guild_prefix VARCHAR(15) DEFAULT 'u!',
    log_channel BIGINT NOT NULL DEFAULT NULL,
    join_channel BIGINT NOT NULL  DEFAULT NULL,
    leave_channel BIGINT NOT NULL DEFAULT NULL,
    PRIMARY KEY (muted_role, guild_prefix, log_channel, join_channel, leave_channel)
    
)

CREATE TABLE users (
    user_id INT(20) NOT NULL DEFAULT 0
)

