-- SQL commands to create database tables for MSA data storage

-- Create Parts Table
CREATE TABLE Parts (
    PartID INT PRIMARY KEY,
    PartName VARCHAR(255) NOT NULL,
    PartDescription TEXT,
    PartCategory VARCHAR(100)
);

-- Create Operators Table
CREATE TABLE Operators (
    OperatorID INT PRIMARY KEY,
    OperatorName VARCHAR(255) NOT NULL,
    OperatorEmail VARCHAR(255) UNIQUE
);

-- Create Instruments Table
CREATE TABLE Instruments (
    InstrumentID INT PRIMARY KEY,
    InstrumentName VARCHAR(255) NOT NULL,
    InstrumentType VARCHAR(100),
    CalibrationDate DATE
);

-- Create Measurements Table
CREATE TABLE Measurements (
    MeasurementID INT PRIMARY KEY,
    PartID INT,
    OperatorID INT,
    InstrumentID INT,
    MeasurementValue DECIMAL(10, 2),
    MeasurementDate DATETIME,
    FOREIGN KEY (PartID) REFERENCES Parts(PartID),
    FOREIGN KEY (OperatorID) REFERENCES Operators(OperatorID),
    FOREIGN KEY (InstrumentID) REFERENCES Instruments(InstrumentID)
);
