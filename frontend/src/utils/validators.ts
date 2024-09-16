import { z } from 'zod';

export const validateEmail = (email: string): boolean => {
  const emailSchema = z.string().email();
  try {
    emailSchema.parse(email);
    return true;
  } catch {
    return false;
  }
};

export const validateSSN = (ssn: string): boolean => {
  const cleanSSN = ssn.replace(/\D/g, '');
  
  if (cleanSSN.length !== 9) {
    return false;
  }

  // Check for known invalid patterns
  const invalidPatterns = ['000', '666', '900-999'];
  if (invalidPatterns.some(pattern => cleanSSN.startsWith(pattern))) {
    return false;
  }

  if (cleanSSN.slice(3, 5) === '00' || cleanSSN.slice(5) === '0000') {
    return false;
  }

  return true;
};

export const validateEIN = (ein: string): boolean => {
  const cleanEIN = ein.replace(/\D/g, '');

  if (cleanEIN.length !== 9) {
    return false;
  }

  // Valid EIN prefixes
  const validPrefixes = [
    '01', '02', '03', '04', '05', '06', '10', '11', '12', '13', '14', '15',
    '16', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '32',
    '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44',
    '45', '46', '47', '48', '50', '51', '52', '53', '54', '55', '56', '57',
    '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '71',
    '72', '73', '74', '75', '76', '77', '80', '81', '82', '83', '84', '85',
    '86', '87', '88', '90', '91', '92', '93', '94', '95', '98', '99'
  ];

  const prefix = cleanEIN.slice(0, 2);
  return validPrefixes.includes(prefix);
};