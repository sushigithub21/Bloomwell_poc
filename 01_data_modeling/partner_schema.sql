-- Base table for all partners
   CREATE TABLE partners (
       partner_id UUID PRIMARY KEY,
       partner_type VARCHAR(20) NOT NULL,   -- WHOLESALER | PHARMACY
       name VARCHAR(255),
       address VARCHAR(255),
       license_no VARCHAR(100),
       contact_email VARCHAR(255),
       contact_phone VARCHAR(20),
       created_at TIMESTAMP,
       updated_at TIMESTAMP
   );

   -- Pharmacy-specific details
   CREATE TABLE pharmacy_details (
       partner_id UUID PRIMARY KEY REFERENCES partners(partner_id),
       dispensing_hours VARCHAR(255)
   );

   -- Wholesaler-specific details
   CREATE TABLE wholesaler_details (
       partner_id UUID PRIMARY KEY REFERENCES partners(partner_id),
       distribution_region VARCHAR(255),
       supply_capacity INT
   );