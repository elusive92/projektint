
-- Checks whether a from_key exists and if it does renames it to to_key.
-- Returns an error code otherwise.

-- Return codes:
-- 10 = Ok, renamed from_key -> to_key
-- 11 = No such from_key

local from_key = KEYS[1]
local to_key = KEYS[2]

if redis.call('exists', from_key) == 1 then
    redis.call('rename', from_key, to_key)
    return 10
else
    return 11
end
