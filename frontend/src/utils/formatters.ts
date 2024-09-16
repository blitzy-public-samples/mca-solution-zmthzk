import { format, parseISO } from 'date-fns';

export function formatCurrency(amount: number, currencyCode: string): string {
  const formatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: currencyCode,
  });
  return formatter.format(amount);
}

export function formatDate(dateString: string, formatString: string): string {
  const parsedDate = parseISO(dateString);
  return format(parsedDate, formatString);
}

export function formatPhoneNumber(phoneNumber: string): string {
  const digitsOnly = phoneNumber.replace(/\D/g, '');
  
  if (digitsOnly.length === 10) {
    return `(${digitsOnly.slice(0, 3)}) ${digitsOnly.slice(3, 6)}-${digitsOnly.slice(6)}`;
  }
  
  return phoneNumber;
}