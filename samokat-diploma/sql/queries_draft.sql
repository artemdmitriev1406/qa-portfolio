-- ЧЕРНОВИК по приложенным требованиям.
-- Конкретные условия SQL-заданий во вложениях отсутствуют.
-- Запросы на учебной PostgreSQL ещё не выполнялись.

-- 1. Число заказов в процессе доставки у каждого курьера.
-- LEFT JOIN сохраняет курьеров, у которых нет таких заказов.
SELECT c."login", COUNT(o."id") AS orders_in_delivery
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o
  ON o."courierId" = c."id"
  AND o."inDelivery" IS TRUE
  AND o."finished" IS NOT TRUE
  AND o."cancelled" IS NOT TRUE
GROUP BY c."id", c."login"
ORDER BY orders_in_delivery DESC, c."login";

-- 2. Статус каждого заказа по приоритету из требований.
-- finished имеет приоритет над cancelled, cancelled — над inDelivery.
SELECT "track",
       CASE
           WHEN "finished" IS TRUE THEN 2
           WHEN "cancelled" IS TRUE THEN -1
           WHEN "inDelivery" IS TRUE THEN 1
           ELSE 0
       END AS status
FROM "Orders"
ORDER BY "track";
