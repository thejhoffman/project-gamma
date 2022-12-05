import { Outlet, Navigate } from "react-router-dom";
import { useGetTokenQuery } from "../store/tokenApi";

const PrivateRoutes = () => {
  const { data: tokenData, isSuccess, isFetching } = useGetTokenQuery();
  let auth = tokenData !== null && isSuccess;
  if (!isFetching)
    return (
      auth ? <Outlet /> : <Navigate to="/login" />
    );
};

export default PrivateRoutes;
