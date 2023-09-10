import { useEffect, useState} from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Box, Button, IconButton, Modal, Radio } from '@mui/material';
import ClearSharpIcon from "@mui/icons-material/ClearSharp";
import { loadQuizList, quizCreate } from '../redux/action';
import { useDispatch, useSelector } from 'react-redux';
import CloudDownloadIcon from '@mui/icons-material/CloudDownload';
import GLOBAL_CONSTANTS from '../../GlobalConstants';
import DeleteIcon from '@mui/icons-material/Delete';


function createData(name, calories, fat, carbs, protein) {
  return { name, calories, fat, carbs, protein};
}

const rows = [
  createData('Frozen yoghurt', 159, 6.0, 50,100),
  createData('Ice cream sandwich', 237, 9.0, 50,100),
  createData('Eclair', 262, 16.0, 50,100),
  createData('Cupcake', 305, 3.7, 50,100),
  createData('Gingerbread', 356, 16.0, 50,100),
];

export default function QuizListing() {
  const dispatch = useDispatch();
  const [open,setOpen] = useState(false);
  const [selectedRow,setselectedRow]=useState(null);
  const { quizList } = useSelector((state) => state.data);

  
  const [profileImage, setProfileImage] = useState([]);
  const handleFileSelect = (event) => {
    setProfileImage(() => event.target.files);
  };

  const onSignUp = () => {
    console.info(profileImage,"profileImage")
    dispatch(quizCreate({file:profileImage,user_id:GLOBAL_CONSTANTS?.user_cred?.user_id}, () => {}));
  };

  const downloadQuiz=()=>{
    console.log("downloadQuiz");
  }

  const handleRowSelection=()=>{
    console.log("testrowselect")
  }

  useEffect(()=>{
dispatch(loadQuizList());
  },[])

  useEffect(()=>{
console.log("quizList",quizList)
  },[quizList])
//   #region image upload 



// useEffect(() => {
//   if (profileImage?.length) {
//     // console.log("files", files);
//     for (let index = 0; index < profileImage?.length; index++) {
//       let reader = new FileReader();
//       reader.readAsDataURL(profileImage[index]);
//       reader.onload = (e) => {
//         // console.log("file", e.target.result);
//         const payload = {
//           data: e.target.result.split(",")[1] 
//         };
//         // console.log(payload, "payload");
//         // dispatch(
//         //   getCSVLink(payload, (resp) => {
//         //     setProfileLink(() => resp?.data?.link);
//         //   })
//         // );
//       };
//     }
//   }
// }, [profileImage]);


  return (
    <div className='grid gap-4 p-4'>
<div className='' >
{selectedRow!=null && <Button variant='contained' color='secondary' onClick={()=>{setOpen(true)}} >Edit Selected Quiz</Button>}
<Button variant='contained' color='secondary' style={{marginLeft:"10px"}} onClick={()=>{setOpen(true)}} >Create Quiz</Button>

</div>
<div className='' >
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead style={{background:"linear-gradient(1deg,#7b24d240 30%, #9c27b050)"}} >
          <TableRow>
            <TableCell>Select</TableCell>
            <TableCell>Ttitle</TableCell>
            <TableCell >Pass Marks</TableCell>
            <TableCell >Lesson to unLock</TableCell>
            <TableCell >Created Date</TableCell>
            <TableCell >Last Updated Date</TableCell>
            <TableCell >Action</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {quizList.map((row) => (
            <TableRow
              key={row.title}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell >
                <Radio onChange={()=>{setselectedRow(row.id)}}  checked={selectedRow==row.id?true:false}></Radio>
              </TableCell>
              <TableCell component="th" scope="row">
                {row.title}
              </TableCell>
              <TableCell>{row.pass_marks}</TableCell>
              <TableCell>{row.next_lessons_to_unlock}</TableCell>
              <TableCell>{row.created_date}</TableCell>
              <TableCell>{row.updated_date}</TableCell>
              <TableCell><DeleteIcon></DeleteIcon></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    </div>

    {open && (
          <Modal
            open={open}
            onClose={()=>{setOpen(false)}}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
          >
            <Box
              style={{
                width: "100vw",
                height: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
              }}
              onClick={() => {
                setOpen(false)
              }}
            >
              <Box
                style={{
                  background: "white",
                  borderRadius: "8px",
                  padding: "8px 12px ",
                  width:"calc(min(600px,100%))",
                  display:"grid",
                  gap:"10px"
                }}
                onClick={(e) => {
                  e.stopPropagation();
                }}
              >

                <div style={{display:"flex",justifyContent:"space-between",alignItems:"center"}} className="font-semibold p-2 text-purple-800" >
                Create Quiz
              <ClearSharpIcon color='secondary' style={{cursor:"pointer"}} onClick={()=>{setOpen(false)}}  />
                </div>
                {/* <Divider  /> */}

              <div className="grid gap-4">

                <div className='grid grid-cols-2 justify-center items-center w-full h-full gap-2   '>
                    <div className='flex flex-col justify-center items-center text-md gap-y-4 text-white font-medium bg-gray-400 rounded p-4 border-2 border-dashed border-gray-200' >
                    Download Sample CSV file from here  
                    
                    <Button endIcon={<CloudDownloadIcon />} style={{color:"white",borderColor:"white"}}  variant='outlined' size='small' > Download </Button>
                    </div>

                    <div className='flex flex-col justify-center items-center text-md gap-y-4 text-white font-medium  bg-purple-600 rounded p-4 border-2 border-dashed border-purple-300 ' >
 Upload the CSV to Create the Quiz in the given sample format 
 <label htmlFor='file' >
 <div  className='text-white border border-white py-1 px-4 rounded flex gap-3 items-center justify-center cursor-pointer'   > Upload <CloudDownloadIcon /> </div>
 </label>
                        <input
                        //   accept="xlxs"
                          type="file"
                          id="file"
                          name="file"
                          className="sr-only"
                          onChange={handleFileSelect}
                        />

                    </div>


               </div>
            </div>
            {/* <Divider /> */}
              <div className='flex justify-end gap-x-4' >
                <Button size="small" variant='outlined' color='secondary' onClick={()=>{setOpen(false)}}  > Cancel </Button>
                <Button size="small" variant='contained' color='secondary' onClick={()=>onSignUp()}> Create </Button>
              </div>

              </Box>
            </Box>
          </Modal>
        )}

</div>

  );
}