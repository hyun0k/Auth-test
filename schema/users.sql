-- 회원 테이블 생성 --
CREATE TABLE IF NOT EXISTS users
(
    `id`            INT UNSIGNED    NOT NULL    AUTO_INCREMENT, 
    `user_id`       VARCHAR(45)     NOT NULL    COMMENT '회원 아이디', 
    `password`      VARCHAR(45)     NOT NULL    COMMENT '비밀번호', 
    `name`          VARCHAR(45)     NOT NULL    COMMENT '회원 이름', 
    `email`         VARCHAR(320)    NOT NULL    COMMENT '이메일 주소', 
    `phone_number`  VARCHAR(11)     NOT NULL    COMMENT '핸드폰 번호', 
     PRIMARY KEY (id)
);

ALTER TABLE users COMMENT '회원';