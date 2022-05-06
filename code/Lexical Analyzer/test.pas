//Código de prueba
program posneg;
uses crt;
var 
 no : integer;
begin
 clrscr;
  write('Enter a number:');
  read(no);
//Comentario de prueba;
  if (no > 0) then
   write('You enter Positive Number')
  else
    if (no < 0) then
     write('You enter Negative number')
    else
      if (no = 0) then
      write('You enter Zero');
{Comentario
de
prueba}
  read;
 end.