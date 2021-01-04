CREATE TABLE Admins (
    adminId INTEGER NOT NULL PRIMARY KEY,
    adminFullName VARCHAR(50) NOT NULL,
    adminNick VARCHAR(50) NOT NULL UNIQUE,
    adminEmail VARCHAR(50) NOT NULL UNIQUE,
    adminCode VARCHAR(50) NOT NULL
);

INSERT INTO Admins(adminFullName,adminNick,adminEmail,
adminCode) VALUES('Orxan Salmanov','oxcik','orxan@gmail.com','asdasd123');

SELECT * FROM Admins;


CREATE TABLE OurBlogs (
    blogId INTEGER NOT NULL PRIMARY KEY,
    blogImage VARCHAR(50) NOT NULL,
    blogTitle VARCHAR(50) NOT NULL UNIQUE,
    blogNutshell VARCHAR(100) NOT NULL,
    blogDetail TEXT NOT NULL,
    blogDate DATE,
    blogAuthor INTEGER NOT NULL,
    CONSTRAINT AdminsBlogs
    FOREIGN KEY (blogAuthor)
    REFERENCES Admins(adminId)
);
SELECT * FROM OurBlogs;

INSERT INTO OurBlogs(blogImage,blogTitle,blogNutshell,
blogDetail,blogAuthor) VALUES('sekil','basliq','kisa ozet','etrafli meqale',1),
('sekil','basliqlar','kisa ozetler','etrafli meqale',2);

CREATE TABLE ContactUs (
    userId INTEGER NOT NULL PRIMARY KEY,
    userName VARCHAR(50) NOT NULL,
    userEmail VARCHAR(50) NOT NULl,
    userSubject VARCHAR(100) NOT NULL,
    userMessage TEXT NOT NULL,
    userDate DATE
);
INSERT INTO ContactUs(userName,userEmail,userSubject,
userMessage) VALUES('adi','emaili','subject fikri','etrafli mesaj'),
('sekil','basliqlar','kisa ozetler','etrafli meqale');
SELECT * FROM ContactUs;