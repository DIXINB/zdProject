import unittest
import csv
import os 
from unittest import mock
from io import StringIO
from unittest.mock import MagicMock,patch,Mock,mock_open
from pprint import pprint
from zdpr.src.lib import GetData,Lump

csvfile=StringIO()
csvfile.seek(0)
fieldnames=['TL','U','T']
writer=csv.DictWriter(csvfile,delimiter=';',fieldnames=fieldnames)
writer.writerow({'TL':1,'U':1,'T':1})
writer.writerow({'TL':1,'U':1,'T':1})
writer.writerow({'TL':1,'U':1,'T':1})
csvfile.seek(0)

class TestEx(unittest.TestCase):
    @mock.patch('zdpr.src.lib.GetData')
    def test_preplt_read (self,mock_fin):                                         
        mock_fin=csvfile
        n_rows,u=GetData.preplt_read(mock_fin)
        self.assertEqual(n_rows,3)    
        self.assertTrue(all(u)) 
              
    @mock.patch('zdpr.src.lib.GetData.preplt_read',
	             mock_preplt_read=Mock())
    def test_open_file (self,mock_preplt_read): 		 
        mock=mock_open(read_data='Bat')             
        mock.return_value.__enter__ = Mock(return_value='Bat')
        mock.return_value.__exit__ = Mock(return_value=False)
        mock_preplt_read.return_value='Good'
        with patch('builtins.open',mock,create=True) as m:
            f,out=GetData.open_file('baz')
            fi=open(f)
            fval=fi.readline()
            print('ЭТО f:',fval)
            print('ЭТО out:',out)
            self.assertEqual(fval,'Bat')
            self.assertEqual(out,'Good')
            GetData.open_file(fval)
            mock_preplt_read.assert_called_with('Bat')
            c=mock_preplt_read.call_args_list
            print('Выз:',c)

stream=StringIO()
runner=unittest.TextTestRunner(stream=stream)
result=runner.run(unittest.makeSuite(TestEx))
print('Tests run',result.testsRun)
print('Errors',result.errors)
pprint(result.failures)
stream.seek(0)
print('Test output\n',stream.read())   
           