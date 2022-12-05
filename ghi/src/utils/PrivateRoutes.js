import { Outlet, Navigate } from "react-router-dom";
import { useGetTokenQuery } from "../store/tokenApi";

const PrivateRoutes = () => {
  const { data: tokenData, isSuccess } = useGetTokenQuery();
  let auth = tokenData !== null && isSuccess;
  return (
    auth ? <Outlet /> : <Navigate to="/login" />
  );
};

export default PrivateRoutes;
