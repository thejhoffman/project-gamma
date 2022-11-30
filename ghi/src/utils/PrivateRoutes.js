import { Outlet, Navigate } from "react-router-dom";
import { useGetTokenQuery } from "../store/tokenApi";

const PrivateRoutes = () => {
  const { data: tokenData } = useGetTokenQuery();
  let auth = tokenData !== null;
  return (
    auth ? <Outlet /> : <Navigate to="/login" />
  );
};

export default PrivateRoutes;
