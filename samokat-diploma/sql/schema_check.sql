-- Только чтение. Сначала проверь реальные таблицы и типы полей.
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name IN ('Couriers', 'Orders')
ORDER BY table_name, ordinal_position;
