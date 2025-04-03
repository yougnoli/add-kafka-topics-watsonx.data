SELECT
    "_partition_id",
    "_partition_offset",
    "_timestamp",
    CAST(json_extract_scalar(_message, '$.timestamp') AS bigint) AS event_timestamp,
    json_extract_scalar(_message, '$.iss_position.latitude') AS latitude,
    json_extract_scalar(_message, '$.iss_position.longitude') AS longitude,
    json_extract_scalar(_message, '$.message') AS status_message
FROM "kafka_catalog"."default"."iss-data";
