-- D .read shaped_test.sql
CREATE TABLE events (document TEXT);

INSERT INTO events VALUES ('{
  "userUID": 123,
  "sex": "female",
  "interactions": {
    "2507": {"timestamp": 1698697114, "rating": 0.75 },
    "6956": {"timestamp": 1687561830, "rating": 0.75 },
    "7562": {"timestamp": 1687561820, "rating": 0.75 },
    "7796": {"timestamp": 0, "rating": 0 },
    "8510": {"timestamp": 0, "rating": 0 },
    "8750": {"timestamp": 0, "rating": 0 },
    "9836": {"timestamp": 0, "rating": 0 },
    "9988": {"timestamp": 0, "rating": 0 },
    "10051": {"timestamp": 0, "rating": 0 }
  }
}');

WITH parsed_interactions AS (
    SELECT
        json_extract_string(document, '$.userUID') AS user_id,
        json_keys(json_extract(document, '$.interactions')) AS item_ids,
        document
    FROM
        events
)

SELECT
    user_id,
    item_id_list.item_ids AS item_id,
    json_extract_string(json_extract(document, '$.interactions'), '$.' || item_id_list.item_ids || '.timestamp') AS created_at,
    json_extract_string(json_extract(document, '$.interactions'), '$.' || item_id_list.item_ids || '.rating') AS label
FROM
    parsed_interactions,
    UNNEST(item_ids) AS item_id_list;