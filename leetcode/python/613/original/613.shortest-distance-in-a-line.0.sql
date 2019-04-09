--
-- @lc app=leetcode id=613 lang=mysql
--
-- [613] Shortest Distance in a Line
--
-- https://leetcode.com/problems/shortest-distance-in-a-line/description/
--
-- database
-- Easy (72.39%)
-- Total Accepted:    11.8K
-- Total Submissions: 16.3K
-- Testcase Example:  '{"headers":{"point":["x"]},"rows":{"point":[[-1],[0],[2]]}}'
--
-- Table point holds the x coordinate of some points on x-axis in a plane,
-- which are all integers.
-- 
-- Write a query to find the shortest distance between two points in these
-- points.
-- 
-- 
-- 
-- 
-- | x   |
-- |-----|
-- | -1  |
-- | 0   |
-- | 2   |
-- 
-- 
-- 
-- The shortest distance is '1' obviously, which is from point '-1' to '0'. So
-- the output is as below:
-- 
-- 
-- 
-- 
-- | shortest|
-- |---------|
-- | 1       |
-- 
-- 
-- 
-- Note: Every point is unique, which means there is no duplicates in table
-- point.
-- 
-- 
-- Follow-up: What if all these points have an id and are arranged from the
-- left most to the right most of x axis?
-- 
-- 
-- 
--
# Write your MySQL query statement below

