USE [Python]
GO

/****** Object:  Table [dbo].[Employee]    Script Date: 9/28/2019 11:55:46 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Employee](
	[EmployeeID] [int] IDENTITY(1,1) NOT NULL,
	[EmployeeName] [varchar](100) NULL,
	[Age] [int] NULL,
	[DateOfBirth] [date] NULL,
	[EmailID] [varchar](100) NULL,
	[MobileNumber] [bigint] NULL,
	[Address] [varchar](150) NULL,
	[City] [varchar](50) NULL,
	[State] [varchar](50) NULL,
	[IsActive] [bit] NULL,
	[CreatedDateTime] [datetime] NULL,
	[CreatedBy] [varchar](100) NULL,
	[ModifiedDateTime] [datetime] NULL,
	[ModifiedBy] [varchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[EmployeeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO