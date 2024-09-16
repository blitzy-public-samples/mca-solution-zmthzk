import { z } from 'zod';

interface EmailMetadata {
  sender: string;
  subject: string;
  body: string;
  receivedAt: Date;
}

interface Attachment {
  type: string;
  filePath: string;
  uploadedAt: Date;
}

interface Merchant {
  legalName: string;
  dbaName: string;
  federalTaxId: string;
  address: string;
  industry: string;
  annualRevenue: number;
}

interface Owner {
  name: string;
  ssn: string;
  address: string;
  dateOfBirth: Date;
  ownershipPercentage: number;
}

interface FundingDetails {
  amountRequested: number;
  useOfFunds: string;
}

interface Application {
  id: string;
  status: string;
  createdAt: Date;
  updatedAt: Date;
  emailMetadata: EmailMetadata;
  attachments: Attachment[];
  merchant: Merchant;
  owners: Owner[];
  fundingDetails: FundingDetails;
}

const ApplicationSchema = z.object({
  id: z.string(),
  status: z.string(),
  createdAt: z.date(),
  updatedAt: z.date(),
  emailMetadata: z.object({
    sender: z.string(),
    subject: z.string(),
    body: z.string(),
    receivedAt: z.date(),
  }),
  attachments: z.array(z.object({
    type: z.string(),
    filePath: z.string(),
    uploadedAt: z.date(),
  })),
  merchant: z.object({
    legalName: z.string(),
    dbaName: z.string(),
    federalTaxId: z.string(),
    address: z.string(),
    industry: z.string(),
    annualRevenue: z.number(),
  }),
  owners: z.array(z.object({
    name: z.string(),
    ssn: z.string(),
    address: z.string(),
    dateOfBirth: z.date(),
    ownershipPercentage: z.number(),
  })),
  fundingDetails: z.object({
    amountRequested: z.number(),
    useOfFunds: z.string(),
  }),
});

export type { Application, EmailMetadata, Attachment, Merchant, Owner, FundingDetails };
export { ApplicationSchema };